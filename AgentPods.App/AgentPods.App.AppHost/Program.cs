var builder = DistributedApplication.CreateBuilder(args);
var currentDir = Directory.GetCurrentDirectory();
var opaPoliciesPath = Path.Combine(currentDir, "docker", "opa", "policies");
var mcpConfigPath = Path.Combine(currentDir, "docker", "mcp", "config");
var mcpDataPath = Path.Combine(currentDir, "data");
// Mongo
var mongo = builder.AddContainer("mongo", "mongo")
                   .WithVolume("mongo_data", "/data/db")
                   .WithEndpoint(27017, targetPort: 27017, name: "mongodb");

// Redis
var redis = builder.AddContainer("redis", "redis")
                   .WithEndpoint(6379, targetPort: 6379, name: "redis");

// Keycloak (use your locally built Keycloak image)
var keycloak = builder.AddContainer("keycloak", "agentpods/keycloak")
                      .WithEndpoint(8080, targetPort: 8080, name: "keycloak");


// OPAL (use your locally built OPAL image)
/*var opal = builder.AddContainer("opal", "agentpods/opal")
                  .WithEndpoint(7002, targetPort: 7002, name: "opal")
                  .WithArgs("run", "--server", "--log-level=info");

var opa = builder.AddContainer("opa", "agentpods/opa")
                 .WithEndpoint(8181, targetPort: 8181, name: "opa")
                 .WithArgs("run", "--server", "--log-level=info", "/policies");*/
               
// AI Orchestrator (local image)
/*var aiOrchestrator = builder.AddContainer("ai-orchestrator", "agentpods/ai-orchestrator")
                            .WithEndpoint(8000, targetPort: 8000, name: "ai-orchestrator")
                            .WithEnvironment("MONGO_URL", mongo.GetEndpoint("mongodb"))
                            .WithEnvironment("REDIS_URL", redis.GetEndpoint("6379"))
                            .WithEnvironment("OPA_URL", opa.GetEndpoint("8181"))
                            .WithEnvironment("KEYCLOAK_URL", keycloak.GetEndpoint("8080"));*/


// AutoGen Studio (local image)
var studio = builder.AddContainer("studio", "agentpods/studio")
                    .WithEndpoint(8081, targetPort: 8081, name: "studio");

// AutoGen Bench (local image — uncomment if you want to enable)
// var bench = builder.AddContainer("bench", "agentpods/bench")
//                    .WithEndpoint(8082, targetPort: 8082, name: "bench");

// Flowise (external image — you can build your own if needed)
var flowise = builder.AddContainer("flowise", "flowiseai/flowise")
                     .WithEndpoint(3000, targetPort: 3000, name: "flowise");

// React UI (if using locally built container or AddProject — optional)
// var reactUI = builder.AddProject("ReactUI", "../ui/react_chat")
//                      .WithExternalHttpEndpoints();



var pg = builder
  .AddContainer("pg", "postgres:15")            // or whatever tag you prefer
  .WithEnvironment("POSTGRES_USER",     "mcpuser")
  .WithEnvironment("POSTGRES_PASSWORD", "mcppass")
  .WithEnvironment("POSTGRES_DB",       "mcpdb")
  .WithVolume("pg_data", "/var/lib/postgresql/data")
  .WithEndpoint(5432, targetPort: 5432, name: "pg");


var mcp = builder
  .AddContainer("mcp", "agentpods/mcp-gateway:latest")
  .WithEndpoint(4444, 4444, name: "mcp")
  .WithEnvironment("DATABASE_URL", "postgresql://mcpuser:mcppass@pg:5432/mcpdb")
  .WithEnvironment("HOST",               "0.0.0.0")
  .WithEnvironment("JWT_SECRET_KEY",     "my-test-key")
  .WithEnvironment("BASIC_AUTH_USER",    "admin")
  .WithEnvironment("BASIC_AUTH_PASSWORD","changeme");

builder.Build().Run();