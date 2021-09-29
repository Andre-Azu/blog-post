function deleteBlog(blogId){
    fetch("/delete-blog",{
        method: 'POST',
        body: JSON.stringify({blogId: blogId}),
        // JSON.stingify turns blogID into a string
    }).then((_res)=>{
        window.location.href="/";
        // 'window.location.href'basically refreshes the page to the main homepage
    });
}