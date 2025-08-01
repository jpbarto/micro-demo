FROM alpine:latest

# Copy the prime-service binary from src directory to /opt in the container
COPY src/fib-service /opt/fib-service

# Make sure the binary is executable
RUN chmod +x /opt/fib-service

# Set the entrypoint to run the binary
ENTRYPOINT ["/opt/fib-service"]