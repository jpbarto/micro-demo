FROM golang:alpine

WORKDIR /opt
COPY src/* /opt/fib-service/

WORKDIR /opt/fib-service
RUN go build -o ./bin/fib-service
# Make sure the binary is executable
RUN chmod +x ./bin/fib-service

# Set the entrypoint to run the binary
ENTRYPOINT ["/opt/fib-service/bin/fib-service"]