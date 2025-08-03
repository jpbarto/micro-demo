FROM alpine:latest

# Copy the prime-service binary from src directory to /opt in the container
COPY src/bin/prime-service /opt/prime-service

# Make sure the binary is executable
RUN chmod +x /opt/prime-service

# Set the entrypoint to run the binary
ENTRYPOINT ["/opt/prime-service"]