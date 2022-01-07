export const login = (email,password) => {

    var isSuccessfull = false;
    var jwt_token = null;
    const credentials = {
        email,
        password
    }
    var requestOptions = {
        method: 'POST',
        body: JSON.stringify(credentials),
        redirect: 'follow',
        mode:'no-cors'

      };
      
      fetch("http://127.0.0.1:8000/api/login/", requestOptions)
        .then(response => response.json())
        .then(result => {
            console.log(result)
            if(result.success)
            {
                isSuccessfull = true;
                jwt_token = result.token
            }
        })
        .catch(error => console.log('error', error));
    if(isSuccessfull)
    {
        return {
            success:true,
            token:jwt_token
        }
    }
    return {
        success:false,
        token:null
    }
}