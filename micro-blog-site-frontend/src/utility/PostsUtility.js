
export const getAllPosts = () => {
    var requestOptions = {
        method: 'GET',
        mode:'cors',
        headers:{
            'Content-type':'Application/json'
        }
      }
    const posts = fetch("/api/getallposts", requestOptions)
        .then(response => response.json())
        .then(result => result.posts)
        .catch(error => console.log('error', error));
   
    if(posts.length !== 0)
    {
        console.log(posts)
        return posts
    }
    return []

}
