```markdown
# Internet Connection Checker

This Python script continuously checks the internet connection status and provides detailed information about the connection. It notifies the user when the connection goes up or down and logs the status changes to a file.

## Features

- **Continuous Monitoring**: The script runs indefinitely, periodically checking the internet connection status.

- **Detailed Information**: Provides information such as IP address, network interface, and latency.

- **Customizable Ping Target**: You can specify the target to ping (default is Google's DNS server).

- **Logging**: Logs the status changes along with timestamps to a log file.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/infoxmax/Internet_Check.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Internet_Check
    ```

3. Run the script:

    ```bash
    python3 internet_checker.py
    ```

4. Customize the ping target (optional):

    Open the script file (`internet_checker.py`) and modify the `PING_TARGET` constant to change the target to ping.

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- This script was inspired by the need for a simple and effective way to monitor internet connectivity.


