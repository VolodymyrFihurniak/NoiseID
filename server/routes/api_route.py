from routes.base_route import BaseRoute


class ApiRoute(BaseRoute):
    def configure_routes(self):
        @self.router.get("/api/info")
        async def api_info():
            """
                Get the version of the API
            """
            return {"message": {"version": "0.0.1"}}

        return self.router
