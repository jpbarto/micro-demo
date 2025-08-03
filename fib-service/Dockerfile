FROM alpine:latest

WORKDIR /opt
COPY src/fib-service /opt/fib-service

# Make sure the binary is executable
RUN chmod +x /opt/fib-service

# Set the entrypoint to run the binary
ENTRYPOINT ["/opt/fib-service"]