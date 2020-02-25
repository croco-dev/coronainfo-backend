import requests
from bs4 import BeautifulSoup
import re
from patients.models import Patient
from feeds.models import Feed
from versions.models import Version
from reports.models import Report
from datetime import date


class Crawler:
    def RepresentsInt(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def get(self):
        for i in range(1, 15):
            req = requests.get(
                f"http://ncov.mohw.go.kr/bdBoardList.do?brdId=1&brdGubun=12&dataGubun=&ncvContSeq=&contSeq=&board_id=&gubun=&pageIndex={i}"
            )
            html = req.text
            bsObject = BeautifulSoup(html, "html.parser")
            for div in bsObject.select("div.onelist"):
                patient = {}
                patient["index"] = re.sub(
                    "\s+", "", div.select("a > ul > li:nth-child(1) > span")[1].text
                )
                patient["infected_route"] = re.sub(
                    "\s+", "", div.select("a > ul > li:nth-child(3) > span")[1].text
                )
                patient_info = re.sub(
                    "\s+", "", div.select("a > ul > li:nth-child(2) > span")[1].text
                ).split("(")
                patient["sex"] = patient_info[0]
                patient["country"] = patient_info[1].split(",")[0]
                birth = int(
                    patient_info[1].split(",")[1].replace("'", "").replace(")", "")
                )
                if birth >= 20:
                  patient["age"] = 121 - birth
                else:
                  patient["age"] = 21 - birth
                patient["date"] = "2020-" + re.sub(
                    "\s+", "", div.select("a > ul > li:nth-child(4) > span")[1].text
                ).replace(".", "-")
                patient["hospital"] = re.sub(
                    "\s+", "", div.select("a > ul > li:nth-child(5) > span")[1].text
                )
                contact = re.sub(
                    "\s+", "", div.select("a > ul > li:nth-child(6) > span")[1].text
                ).split("(")[0]
                if contact != "확인중":
                    patient["contact_count"] = contact
                else:
                    patient["contact_count"] = 0
                if self.RepresentsInt(patient["infected_route"].split("번째환자")[0]):
                    patient["second_infection"] = patient["infected_route"].split(
                        "번째환자"
                    )[0]
                elif self.RepresentsInt(patient["infected_route"].split("번째확진자")[0]):
                    patient["second_infection"] = patient["infected_route"].split(
                        "번째확진자"
                    )[0]
                else:
                    patient["second_infection"] = None
                if patient["hospital"] == "격리해제":
                    patient["status"] = "완치"
                else:
                    patient["status"] = "확진 및 격리"
                patient_row, created = Patient.objects.update_or_create(
                    index=patient["index"], defaults=patient
                )
                feed = Feed(
                    index=patient["index"],
                    status=patient["status"],
                    log_type="patient",
                    date=date.today(),
                    contact_count=patient["contact_count"],
                    second_infection=patient["second_infection"],
                    place=patient["hospital"],
                )
        version = Version(date=date.today())
        version.save()
        return version

    def temp(self):
        req = requests.get("http://ncov.mohw.go.kr/index_main.jsp")
        html = req.text
        bsObject = BeautifulSoup(html, "html.parser")
        db_count = Patient.objects.count()
        crawl_count = int(
            bsObject.select("div.co_cur > ul > li")[0].a.text.split(" ")[0]
        )
        cure_count = int(
            bsObject.select("div.co_cur > ul > li")[1].a.text.split(" ")[0]
        )
        death_count = int(
            bsObject.select("div.co_cur > ul > li")[2].a.text.split(" ")[0]
        )
        if db_count < crawl_count:
            for i in range(db_count + 1, crawl_count + 1):
                patient = Patient(index=i, status="확진 및 격리", date=date.today())
                patient.save()
                feed = Feed(
                    index=i, log_type="patient", date=date.today(), status="확진 및 격리"
                )
                feed.save()
        report = Report(cure_count=cure_count, death_count=death_count, patient_count=crawl_count)
        report.save()
        version = Version(date=date.today())
        version.save()
        return Version.objects.first()

