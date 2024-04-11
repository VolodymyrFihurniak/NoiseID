from routes.base_route import BaseRoute


class AuthRoute(BaseRoute):
    def configure_routes(self):
        @self.router.get("/api/registration")
        async def auth_registration():
            """
                Register a new user
            """
            return {"message": "registration"}

        @self.router.get("/api/login")
        async def auth_login():
            """
                Login a user
            """
            return {"message": "login"}

        return self.router
