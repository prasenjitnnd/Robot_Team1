import zipfile
import xml.etree.ElementTree as ET
import os
import shutil
import time
import stat
import chromedriver_autoinstaller
import requests
import json
import jsonpath



def check_values(notification_flag_original, delete_folder_check, unused_client_value, unprint_job_value,
                 late_bind_flag, print_job_value, queue_name):
    global notification_flag, delete_folder_flag
    global check1, check2, check3, check4, check5, check6, check7, check8
    if os.path.exists("C:\\Users\\scmselenium\\Downloads\\customPackage.zip"):
        with zipfile.ZipFile(r"C:\Users\scmselenium\Downloads\customPackage.zip", "r") as zip_ref:
            zip_ref.extractall(r"C:\Users\scmselenium\Downloads\customPackage")

        tree = ET.parse(r"C:\Users\scmselenium\Downloads\customPackage\configuration.xml")
        root = tree.getroot()

        for notification in root.iter('DisplayNotifications'):
            notification_flag = str(notification.text)
            if notification_flag == str(notification_flag_original).lower():
                print("Notification set correctly to " + notification_flag)
                check1 = "True"
            else:
                check1 = "False"
                print("Did not configure correctly")

        for deletefolder in root.iter('DeleteEmptyUserFolders'):
            delete_folder_flag = str(deletefolder.text)

            if delete_folder_flag == str(delete_folder_check).lower():
                print("Delete folder flag set correctly to " + delete_folder_flag)
                check2 = "True"
            else:
                check2 = "False"
                print("Did not configure correctly")

        if str(delete_folder_check).lower() == "true":
            for deletefolderspan in root.iter('DeleteEmptyUserFoldersLifespan'):
                delete_folder_span = int(deletefolderspan.text)
                if delete_folder_span == int(unused_client_value):
                    print("Delete folder value is " + str(delete_folder_span))
                    check3 = "True"
                else:
                    check3 = "False"
                    print("Did not configure correctly")
        else:
            for deletefolderspan in root.iter('DeleteEmptyUserFoldersLifespan'):
                delete_folder_span = int(deletefolderspan.text)
                if delete_folder_span == 7:
                    print("Default value retained for Empty User Folder span")
                    check3 = "True"
                else:
                    print("Default value not retained for Empty User Folder span")
                    check3 = "False"

        for unprintspan in root.iter('UnprintedJobsLifespan'):
            unprint_job_span = int(unprintspan.text)
            if unprint_job_span == int(unprint_job_value):
                print("Print and Keep life for unprinted jobs is " + str(unprint_job_span))
                check4 = "True"
            else:
                print("Not configured correctly")
                check4 = "False"

        for printspan in root.iter('PrintAndKeepLifespan'):
            print_job_span = int(printspan.text)
            if print_job_span == int(print_job_value):
                print("Print and Keep life span for printed jobs is " + str(print_job_span))
                check5 = "True"
            else:
                print("Not configured correctly")
                check5 = "False"

        for latebinding in root.iter('LateBindingEnabled'):
            late_binding_flag = str(latebinding.text)

            if late_binding_flag == str(late_bind_flag).lower():
                print("Late Binding flag set to " + late_binding_flag)
                check6 = "True"
            else:
                print("Did not configure correctly")
                check6 = "False"

        for defaultqueue in root.iter('DefaultQueue'):
            default_print_queue = str(defaultqueue.text)
            if str(queue_name) == 'True':
                default__name = "LPMCloud"
            else:
                default__name = "LPMServerless"
            if default__name == default_print_queue:
                print("Default queue name set is : " + str(default_print_queue))
                check7 = "True"
            else:
                print("Default queue name set is : " + str(default_print_queue))
                check7 = "False"

        file_path = "C:\\Users\\scmselenium\\Downloads\\customPackage.zip"
        os.chmod(file_path, stat.S_IWRITE)
        os.remove(file_path)
        folder_path = "C:\\Users\\scmselenium\\Downloads\\customPackage\\"
        os.chmod(folder_path, stat.S_IWRITE)
        shutil.rmtree(folder_path, onerror=check_write_error)

        if check1 == "False" or check2 == "False" or check3 == "False" or check4 == "False" or check5 == "False" or\
                check6 == "False" or check7 == "False":
            return "False"
        else:
            return "True"
    else:
        print("File download failed")
        return "False"


def download_wait(filename):
    path_to_downloads = "C:\\Users\\scmselenium\\Downloads"
    while not os.path.exists(path_to_downloads + "\\" + filename):
        pass
    if os.path.isfile(path_to_downloads + '\\' + filename):
        return filename + " File Downloaded"


def download_wait_mac_saas(url):

    if "us" in url:
        base_url = "https://apis.dev.us.cloud.onelxk.co/cpm/client-download-service/package/current/versions"
        payload = {}
        headers = {}

        response = requests.request("GET", base_url, headers=headers, data=payload)
        #print(response.text)
        json_response = json.loads(response.content)
        filename = jsonpath.jsonpath(json_response, 'lpmcWithMacColorDriver')
        filename=filename[0]

    else:
        base_url = "https://apis.dev.eu.cloud.onelxk.co/cpm/client-download-service/package/current/versions"
        payload = {}
        headers = {}

        response = requests.request("GET", base_url, headers=headers, data=payload)
        #print(response.text)
        json_response = json.loads(response.content)
        filename = jsonpath.jsonpath(json_response, 'lpmcWithMacColorDriver')
        filename=filename[0]
    path_to_downloads = "C:\\Users\\scmselenium\\Downloads"
    print(filename)

    while not os.path.exists(path_to_downloads + "//" + filename):
        pass
    if os.path.isfile(path_to_downloads + '//' + filename):
        print("Downloaded")
        os.remove(path_to_downloads + "/" + filename)
        return filename


def download_wait_mac_serverless(url):
    if "us" in url:
        base_url = "https://apis.dev.us.cloud.onelxk.co/cpm/client-download-service/package/current/versions"
        payload = {}
        headers = {}

        response = requests.request("GET", base_url, headers=headers, data=payload)
        json_response = json.loads(response.content)
        filename = jsonpath.jsonpath(json_response, 'lpmcServerlessWithMacColorDriver')
        filename=filename[0]

    else:
        base_url = "https://apis.dev.eu.cloud.onelxk.co/cpm/client-download-service/package/current/versions"
        payload = {}
        headers = {}

        response = requests.request("GET", base_url, headers=headers, data=payload)
        #print(response.text)
        json_response = json.loads(response.content)
        filename = jsonpath.jsonpath(json_response, 'lpmcServerlessWithMacColorDriver')
        filename = filename[0]
    path_to_downloads = "C://Users//scmselenium//Downloads"
    while not os.path.exists(path_to_downloads + "//" + filename):
        pass
    if os.path.isfile(path_to_downloads + '//' + filename):
        print("Downloaded")
        os.remove(path_to_downloads + "/" + filename)
        return filename


def download_wait_win_saas(url):
    if "us" in url:
        base_url = "https://apis.dev.us.cloud.onelxk.co/cpm/client-download-service/package/current/versions"
        payload = {}
        headers = {}

        response = requests.request("GET", base_url, headers=headers, data=payload)
        json_response = json.loads(response.content)
        filename = jsonpath.jsonpath(json_response, 'lpmcWithPCLXLDriver')
        filename = filename[0]
    else:
        base_url = "https://apis.dev.eu.cloud.onelxk.co/cpm/client-download-service/package/current/versions"
        payload = {}
        headers = {}

        response = requests.request("GET", base_url, headers=headers, data=payload)
        json_response = json.loads(response.content)
        filename = jsonpath.jsonpath(json_response, 'lpmcWithPCLXLDriver')
        filename = filename[0]
    path_to_downloads = "C://Users//scmselenium//Downloads"
    while not os.path.exists(path_to_downloads + "//" + filename):
        pass
    if os.path.isfile(path_to_downloads + '//' + filename):
        print("Downloaded")
        os.remove(path_to_downloads + "/" + filename)
        return filename


def download_wait_win_hybrid(url):
    if "us" in url:
        base_url = "https://apis.dev.us.cloud.onelxk.co/cpm/client-download-service/package/current/versions"
        payload = {}
        headers = {}

        response = requests.request("GET", base_url, headers=headers, data=payload)
        json_response = json.loads(response.content)
        filename = jsonpath.jsonpath(json_response, 'lpmcServerlessWithPCLXLDriver')
        filename = filename[0]
    else:
        base_url = "https://apis.dev.eu.cloud.onelxk.co/cpm/client-download-service/package/current/versions"
        payload = {}
        headers = {}

        response = requests.request("GET", base_url, headers=headers, data=payload)
        json_response = json.loads(response.content)
        filename = jsonpath.jsonpath(json_response, 'lpmcServerlessWithPCLXLDriver')
        filename = filename[0]

    path_to_downloads = "C://Users//scmselenium//Downloads"
    while not os.path.exists(path_to_downloads + "//" + filename):
        pass
    if os.path.isfile(path_to_downloads + '//' + filename):
        print("Downloaded")
        os.remove(path_to_downloads + "/" + filename)
        return filename


def check_queue_name(url, saas_name, hybrid_name, driver_name):
    global notification_flag, delete_folder_flag, saas_check, hybrid_check, file_exist
    time.sleep(5)
    if "eu" in url:
        driver_name_url = driver_name.replace("US", "EU")
    else:
        driver_name_url = driver_name

    if os.path.exists("C:\\Users\\scmselenium\\Downloads\\customPackage.zip"):
        with zipfile.ZipFile("C:\\Users\\scmselenium\\Downloads\\customPackage.zip", "r") as zip_ref:
            zip_ref.extractall("C:\\Users\\scmselenium\\Downloads\\customPackage")

        tree = ET.parse("C:\\Users\\scmselenium\\Downloads\\customPackage\\configuration.xml")
        root = tree.getroot()

        folder_path = "C:\\Users\\scmselenium\\Downloads\\customPackage\\"
        file_list = os.listdir(folder_path)
        print(driver_name_url)
        for i in range(len(file_list)):
            print(file_list[i])
            if file_list[i] == driver_name_url:
                file_exist = "True"
                print("Correct file found")
            else:
                file_exist = "False"
                print("Incorrect file found")
        for saas_queue in root.iter('CloudPrintQueueName'):
            saas_print_queue = str(saas_queue.text)

            if str(saas_name) == str(saas_print_queue):
                saas_check = "True"
                print("SAAS queue name set is : " + saas_print_queue)
            else:
                print("SAAS queue name set is incorrect : " + saas_print_queue)
                saas_check = "False"
        for hybrid_queue in root.iter('HybridPrintQueueName'):
            hybrid_print_queue = str(hybrid_queue.text)
            print(hybrid_print_queue)
            print(hybrid_name)
            if str(hybrid_name) == str(hybrid_print_queue):
                print("Hybrid queue name set is : " + hybrid_print_queue)
                hybrid_check = "True"
            else:
                print("Hybrid queue name set is incorrect : " + hybrid_print_queue)
                hybrid_check = "False"

        file_path = "C:\\Users\\scmselenium\\Downloads\\customPackage.zip"
        os.chmod(file_path, stat.S_IWRITE)
        os.remove(file_path)
        folder_path = "C:\\Users\\scmselenium\\Downloads\\customPackage\\"
        os.chmod(folder_path, stat.S_IWRITE)
        shutil.rmtree(folder_path, onerror=check_write_error)

        if saas_check == "True" and hybrid_check == "True" and file_exist == "True":
            print("Queue name  and driver data stream set correctly")
            return "Correct"
        else:
            print("Queue name or driver data stream set incorrectly")
            return "Incorrect"
    else:
        print("File Download fails")


def check_msi_name(url, drivername):
    global file_path
    file_path = "C:\\Users\\scmselenium\\Downloads\\customPackage.zip"
    os.chmod(file_path, stat.S_IWRITE)

    if os.path.exists("C:\\Users\\scmselenium\\Downloads\\customPackage.zip"):
        with zipfile.ZipFile("C:\\Users\\scmselenium\\Downloads\\customPackage.zip", "r") as zip_ref:
            zip_ref.extractall("C:\\Users\\scmselenium\\Downloads\\customPackage")

        path_folder = "C:\\Users\\scmselenium\\Downloads\\customPackage"
        os.chmod(path_folder, stat.S_IWRITE)
        print(os.listdir(path_folder))
        if os.path.exists("C:\\Users\\scmselenium\\Downloads\\customPackage" + "\\" + drivername):
            file_path = "C:\\Users\\scmselenium\\Downloads\\customPackage.zip"
            os.chmod(file_path, stat.S_IWRITE)
            os.remove(file_path)
            folder_path = "C:\\Users\\scmselenium\\Downloads\\customPackage\\"
            os.chmod(folder_path, stat.S_IWRITE)
            shutil.rmtree(folder_path, onerror=check_write_error)
            return "Correct file found : " + drivername

        else:
            file_path = "C:\\Users\\scmselenium\\Downloads\\customPackage.zip"
            os.chmod(file_path, stat.S_IWRITE)
            os.remove(file_path)
            folder_path = "C:\\Users\\scmselenium\\Downloads\\customPackage\\"
            os.chmod(folder_path, stat.S_IWRITE)
            shutil.rmtree(folder_path, onerror=check_write_error)
            return "Incorrect file found : " + drivername


def check_file_list():
    # result = []
    search_path="C:\\users\\scmselenium\\Downloads\\"
    # #print(os.listdir(search_path))
    # filename="chromedriver.exe"
    # #os.rename("C:\\users\\scmselenium\\ChromeDriver","C:\\users\\scmselenium\\ChromeDrv")
    # #shutil.copy("C:\\users\\scmselenium\\Downloads\\chromedriver_win32\\chromedriver.exe","C:\\users\\scmselenium\\ChromeDriver\\")
    # #os.remove("C:\\Users\\scmselenium\\chromedriver.exe")
    # #os.remove("C:\\Users\\scmselenium\\ChromeDriver_old\\chromedriver.exe")
    #os.remove("C:\\users\\scmselenium\\Downloads\\LPMC_ServerlessEU_2.3.994.0_UPD_2.15_Win_PCLXL_1.0.321.exe")
    # for root, dir, files in os.walk(search_path):
    #     if filename in files:
    #         result.append(os.path.join(root, filename))
    # print(result)
    #path = "C:\\Users\\scmselenium\\ChromeDrv"
    print(os.listdir(search_path))
    #os.remove("C:\\users\\scmselenium\\Downloads\\customPackage (1).zip")
    #os.remove("C:\\users\\scmselenium\\Downloads\\customPackage (2).zip")
    #os.remove("C:\\users\\scmselenium\\Downloads\\customPackage (3).zip")
    #os.remove("C:\\users\\scmselenium\\Downloads\\Unconfirmed 542417.crdownload")
    os.remove("C:\\users\\scmselenium\\Downloads\\Unconfirmed 47064.crdownload")
    os.remove("C:\\users\\scmselenium\\Downloads\\LPMCServerlessEU_1.1.1454_GenDriver_1.0.70_Mac_Color_1.1.205.pkg")
    os.remove("C:\\users\\scmselenium\\Downloads\\LPMC_ServerlessEU_2.3.997.0_UPD_2.15_Win_PCLXL_1.0.325.exe")

    print(os.listdir(search_path))
    #print(os.environ)
    #chromedriver_autoinstaller.install()


def check_chrome_webdriver():

    chromedriver_autoinstaller.install()


def check_write_error(func, path, exc_info):
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)


def list_files():
    folder_path = r"C:\Users\neogis\Downloads\customPackage"
    file_list = os.listdir(folder_path)
    print(len(file_list))
