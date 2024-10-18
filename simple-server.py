import http.server
import socketserver

# Set the port you want the server to listen on
PORT = 80


# Create a handler to serve simple HTTP requests with a visit counter
class CustomHandler(http.server.SimpleHTTPRequestHandler):
    visit_count = 0

    def do_GET(self):
        # Increment the visit count each time the page is accessed
        CustomHandler.visit_count += 1

        # Respond with a basic HTML page showing the visit count and a cat text picture
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(
            f"<html><head><title>Ping Count</title></head><body>".encode("utf-8")
        )
        self.wfile.write(
            f"<h1>This page has been accessed {CustomHandler.visit_count} times.</h1>".encode(
                "utf-8"
            )
        )
        self.wfile.write(
            f"<pre>" f"  /\_/\  \n" f" ( o.o ) \n" f"  > ^ <  \n" f"</pre>".encode(
                "utf-8"
            )
        )
        self.wfile.write(f"</body></html>".encode("utf-8"))


def main():
    # Set up the server
    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        import socket

        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        print(
            f"Serving HTTP on IP {ip_address} and port {PORT} (http://{ip_address}:{PORT}) ..."
        )
        try:
            # Keep the server running to handle requests
            httpd.serve_forever()
        except KeyboardInterrupt:
            # Stop the server gracefully
            print("\nShutting down the server...")
            httpd.server_close()


if __name__ == "__main__":
    main()

