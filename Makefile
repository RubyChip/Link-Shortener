compose-start: ## Start local docker-compose deployment
	@echo "Starting local deployment..."
	@echo
	docker compose up -d --build
	@echo "SWAGGER: http://localhost:80/docs"
	@echo
	@echo "Done!"
