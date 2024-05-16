<h3 align="center">Thrift Example Project</h3>

## 🧐 About <a name = "about"></a>

This personal project is designed to provide hands-on experience with Apache Thrift. It is structured into three main components:

### Match Server and Save Client
- **Match Server**: Initiates matching processes every second, considering the absolute score in conjunction with the starting time.
- **Save Client**: Sends save requests to a `save_data` server to persist matching results.

### Game Client
- Manages user data through a command-line interface (CLI), allowing users to be added or removed dynamically.

### Save Server
- Receives and persists successful match results from the Match Server to a designated storage server.
