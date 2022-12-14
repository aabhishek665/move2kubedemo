#   Copyright IBM Corporation 2020
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from flask import Flask, jsonify

simpleRestApiApp = Flask (__name__)

@simpleRestApiApp.route("/hello")
def hello():
    return jsonify(message="This is a Python REST API")

# respond to all paths
@simpleRestApiApp.errorhandler(404)
def handle_404(e):
    return jsonify(message="This is a Python REST API")

if __name__ == "__main__":
    simpleRestApiApp.run(host='0.0.0.0', port=8080)
