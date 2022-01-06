import React,{useState} from "react";

import './styles.css'
import { authenticate } from "../../utility/AuthUtility";

const Login = () => {

    const [email,setEmail] = useState("");
    const [password,setPassword] = useState("");

    const handleLogin = () =>
    {
        authenticate(email,password)
    }

    return(
        <div className="login_form_container">
            <h1>Login</h1>
            <table>
                <tr>
                    <td>
                        <label for='email'>Email</label>
                    </td>
                    <td>
                        <input onChange={e => setEmail(e.target.value)} type='email' name="email"/>
                    </td>
                </tr>
                <tr>
                    <td>
                        <label for='password'>Password</label>
                    </td>
                    <td>
                        <input onChange={e => setPassword(e.target.value)} type='password' name='password'/>
                    </td>
                </tr>
            </table>
            <button onClick={handleLogin}>Login</button>
        </div>
    )
}

export default Login;