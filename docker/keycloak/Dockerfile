# Use official Keycloak base image
FROM quay.io/keycloak/keycloak:24.0.1

# Set admin credentials for development
ENV KEYCLOAK_ADMIN=admin
ENV KEYCLOAK_ADMIN_PASSWORD=adminpass

# Copy realm export file into Keycloak import location
COPY realm-export.json /opt/keycloak/data/import/realm-export.json

# Expose Keycloak default port
EXPOSE 8080

# Run Keycloak in dev mode and import the realm
CMD ["start-dev", "--import-realm"]