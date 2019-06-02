import http.server
import subprocess

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        self.do_HEAD()
        output = "<xmp>"
        if self.path == "/":
        	result = self.run_iw_info()
        else:
            value=self.path
            try:
                value = int(value.replace('/',''))*100
                if value > 3200:
                    value = 3200
                elif value < 0:
                    value = 0
                value = str(value)
            except:
                result = "\r\nWrong input, only numbers between 0-31"
            else:
                command = "sudo iw dev wlan0 set txpower limit".split()
                command.append(value)
                output += "\r\nSetting txpower to " + value + '\r\n\r\n'
                subprocess.run(command)
                output += "Done\r\n\r\n"
                result = self.run_iw_info()

        output += result + "</xmp>"
        self.wfile.write(bytes(output,encoding="utf-8"))

    def run_iw_info(self):
        return subprocess.run('iw wlan0 info'.split(), stdout=subprocess.PIPE).stdout.decode('utf-8')


if __name__ == "__main__":
    ip = "0.0.0.0"
    port = 8888
    server = http.server.HTTPServer((ip, port), MyHandler)
    server.serve_forever()
