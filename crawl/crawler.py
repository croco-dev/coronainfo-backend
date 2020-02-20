import requests
from bs4 import BeautifulSoup
import re
from patients.models import Patient
from versions.models import Version
from datetime import date


class Crawler:
    def RepresentsInt(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def get(self):
        req = requests.get("http://ncov.mohw.go.kr/bdBoardList.do?brdId=1&brdGubun=12")
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
            birth = int(patient_info[1].split(",")[1].replace("'", "").replace(")", ""))
            patient["age"] = 120 - birth
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
            if self.RepresentsInt(patient["infected_route"].split("번째환자")[0]):
                patient["second_infection"] = patient["infected_route"].split("번째환자")[0]
            elif self.RepresentsInt(patient["infected_route"].split("번째확진자")[0]):
                patient["second_infection"] = patient["infected_route"].split("번째확진자")[
                    0
                ]
            if patient["hospital"] == "격리해제":
                patient["status"] = "완치"
            else:
                patient["status"] = "확진 및 격리"
            patient_row, created = Patient.objects.update_or_create(
                index=patient["index"], defaults=patient
            )
        version = Version(date=date.today())
        version.save()
        return version
        pass

