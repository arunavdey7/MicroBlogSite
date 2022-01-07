
export const login = (email,password) => {

    
    const credentials = {
        email,
        password
    }
    var requestOptions = {
        method: 'POST',
        body: JSON.stringify(credentials),
        mode:'cors',
        headers:{
            'Content-type':'Application/json'
        }
      }
      
      fetch("/api/login/", requestOptions)
        .then(response => response.json())
        .then(result => {
            if(result.success)
            {
                var jwt_token = result.token
                localStorage.setItem('token',jwt_token)
            }
        })
        .catch(error => console.log('error', error));
    
}