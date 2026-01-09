
def vehicle_details(patientname, doctorname, time):
    result = (
        f"patientname: {patientname}\n"
        f"doctorname: {doctorname}\n"
        f"time: {time}
    )
    return result


if __name__ == "__main__":
   
    print(vehicle_details("raju", "raja", 10/2/2026))
