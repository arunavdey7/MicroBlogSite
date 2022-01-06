import { login } from "./LoginUtility";

export const authenticate = (email,password) => {
    var loginStatus = login(email,password)
    console.log(loginStatus)
}