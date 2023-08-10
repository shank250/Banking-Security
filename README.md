# Physical Security Program for Banks - Weapon Detection and Guard Identification

This program is designed to enhance the physical security of banks by detecting the presence of weapons and harmful equipment within the bank premises. Additionally, it utilizes face and body posture detection to identify security guards present in the vicinity.

## Features

- **Weapon Detection:** The program employs advanced image processing techniques to detect the presence of weapons and harmful equipment within the bank premises. This includes firearms, knives, explosive devices, and more.

- **Guard Identification:** Using facial recognition and body posture analysis, the program identifies security guards present in the area. This ensures that the presence of guards is accounted for and distinguished from potential threats.

- **Real-time Monitoring:** The program continuously analyzes video feeds from surveillance cameras in real-time, providing immediate alerts and notifications in case of detected threats or unidentified guards.

- **Alerts and Reporting:** In case of a potential threat detection or an unrecognized guard, the program generates alerts to the security personnel. Moreover, it compiles comprehensive reports for security analysis and incident investigation.

## Requirements

- **Python 3.x:** Ensure that you have Python 3.x installed on your system.

- **Libraries:** The program relies on specific libraries for image processing, facial recognition, and posture detection. Install the required libraries using the following command:

  ```bash
  pip install requirements.txt
  ```

## Usage

1. **Run the Program:** Execute the program by running the appropriate script. The program will start analyzing video feeds from the designated surveillance cameras.

2. **Threat Detection:** The program will continuously monitor the video feeds for the presence of weapons and harmful equipment. Upon detection, it will trigger an alert and provide information about the detected threat.

3. **Guard Identification:** Using face and body posture detection, the program will identify security guards present in the area. It will distinguish them from potential threats and provide information about their presence.

4. **Alerts and Reporting:** When a potential threat is detected or an unrecognized guard is identified, the program will generate real-time alerts. It will also compile detailed reports for further analysis and reporting.

5. **Configurations:** You can configure parameters such as detection sensitivity, alert thresholds, and camera inputs in the configuration file (`config.ini`).

## Configuration

- **Camera Inputs:** Specify the camera feeds to be analyzed in the configuration file.

- **Detection Parameters:** Adjust the sensitivity of weapon detection and guard identification according to the specific environment.

## Future Enhancements

This program serves as a foundation for enhancing physical security in banks. Future enhancements could include:

- **Multiple Camera Support:** Extend the program to handle multiple surveillance cameras simultaneously.

- **Integration with Security Systems:** Integrate the program with existing security systems for automated responses to threats.

- **Machine Learning:** Implement machine learning techniques to improve accuracy in weapon detection and guard identification.

- **User Interface:** Develop a graphical user interface for easy program setup and monitoring.

## Contributions

Contributions are welcomed! If you have ideas for improvements or new features, feel free to create a pull request.

## License

This program is released under the [MIT License](LICENSE).

---

Please ensure that you have thoroughly reviewed and understood the documentation before deploying the program. If you encounter any issues or have inquiries, contact me at [shashank21005@gmail.com](mailto:shashank21005@gmail.com).
