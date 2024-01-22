import { NextRequest } from "next/server";

export default async function middleware(req: NextRequest) {
    const google_user_data = req.cookies.get("google_user_data");
    const picture = req.cookies.get("picture");
    const email = req.cookies.get("email");
    const name = req.cookies.get("name");

    console.log("MIDDLEWARE.COOKIES: google_user_data", google_user_data);
    console.log("MIDDLEWARE.COOKIES: picture", picture);
    console.log("MIDDLEWARE.COOKIES: email", email);
    console.log("MIDDLEWARE.COOKIES: name", name);

  
  // console.log("MIDDLEWARE.TS: PATHNAME", req.nextUrl.pathname);
  const { nextUrl } = req;

  // console.log("[nextUrl] @middleware", nextUrl);
  console.log("[nextUrl.pathname] @middleware", nextUrl.pathname);

}

export const config = {
  matcher: ["/((?!.+\\.[\\w]+$|_next).*)", "/"],
};
