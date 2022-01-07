import { login } from "./LoginUtility";

export const authenticate = (email,password) => {
   login(email,password)
   if(localStorage.getItem('token') != null)
   {
       return true
   }
   return false;
}