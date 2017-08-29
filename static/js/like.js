var like_post = function(url_like, csrf_token, post_id){
    $.ajax({
      type: "POST",
      url: url_like,
      data : { id : post_id, csrfmiddlewaretoken: csrf_token },
      success : function(response){
        $('#'+post_id).text(response.likes_count);
        if (response.is_liked) {
            $('#'+post_id).next('.like_button').children('.material-icons').attr('style','color:#26a69a');
        } else {
          $('#'+post_id).next('.like_button').children('.material-icons').attr('style', 'color:#9b9b9b');
        }
      }
    });
};
