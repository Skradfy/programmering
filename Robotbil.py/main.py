from mainInterface import MainInterface
from motor import MotorController
from disciplineSelect import DisciplineSelect
from wallFollow import WallFollow
from wallFollowInterface import WallFollowInterface
from lineFollow import LineFollow
from lineFollowInterface import LineFollowInterface
from sumo import Sumo
from sumoInterface import SumoInterface
from remote import RemoteControl
from remoteInterface import RemoteInterface
from powerManagement import PowerManagement
from errorHandling import ErrorHandling
from testAndCalibration import TestAndCalibration
from userInterfaceImprovements import UserInterface
from network import Network

def main():
    # Initialisér systemkomponenter
    main_interface = MainInterface()
    motor_controller = MotorController()
    discipline_selector = DisciplineSelect()
    wall_follow = WallFollow()
    line_follow = LineFollow()
    sumo = Sumo()
    remote_control = RemoteControl()
    power_management = PowerManagement()
    error_handler = ErrorHandling()
    test_calibration = TestAndCalibration()
    network = Network()

    # Vælg disciplin
    discipline_selector.display_disciplines()
    discipline = int(input("Select a discipline by number: "))
    selected_discipline = discipline_selector.select_discipline(discipline)

    # Aktiver disciplin baseret på brugerens valg
    if selected_discipline == "Wall Follow":
        wall_follow_interface = WallFollowInterface(wall_follow)
        wall_follow_interface.start()
        # Brug motorlogik til at bevæge robotten
        motor_controller.robotMoveLogic("forward")

    elif selected_discipline == "SUMO Battle":
        sumo_interface = SumoInterface(sumo)
        sumo_interface.start()
        motor_controller.robotMoveLogic("forward")

    elif selected_discipline == "Line Follow":
        line_follow_interface = LineFollowInterface(line_follow)
        line_follow_interface.start()
        motor_controller.robotMoveLogic("forward")

    elif selected_discipline == "Remote Control":
        remote_interface = RemoteInterface(remote_control)
        remote_interface.move_forward()
        remote_interface.stop()

    else:
        print("Invalid discipline selected.")

    # Kør tests og kalibrering
    test_calibration.run_tests()
    test_calibration.calibrate()

    # Overvåg batteriniveau
    power_management.check_battery()

    # Simuler fejl og log dem
    try:
        raise ValueError("Simulated error!")
    except Exception as e:
        error_handler.handle_error(e)

if __name__ == "__main__":
    main()
