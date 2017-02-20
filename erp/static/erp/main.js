// Globals
var USER = '';
var CURRENT_USER = '{{ user.pk }}'
var USER_FLAG = 0;
var USER_DEL = '';
var USER_ADD = '';
var USER_EDIT = '';
var USER_URL = '/erp';
var USER_CONFIG = {
    add:{url:"/customer_add/",msg:"添加成功！"},
    edit:{url:"/customer_edit/",msg:"已更新资料！"},
    del:{url:"/customer_del/",msg:"已删除！"}
};


// ******************** Functions  *********************/

function user_event(){
  $("#userlist tr button").each(function (i) {
    $(this).click(function(){
      console.log("Origin User Value:"+USER);
      USER=$(this).parents("tr").attr('name')
      console.log("索引："+$(this).index()+"\nUser:"+USER);
      //alert("内容："+$(this).parents("tr").html());
     });
  });
};

// Links Ajax request
$("a.mainLink").each(function (i) {
    $(this).click(function(e){
      e.preventDefault();
      var url = $(this).attr('href');
      var data = {}
      console.log("This Link:"+url);
      console.log($(this));
      axios.post(url, data,AXIOS_CONFIG).then(function (response) {
    		  console.log(response.data);
          widget = response.data
    	  });
     });
});

$("#ajaxtest").each(function (i) {
    $(this).click(function(e){
      e.preventDefault();
      var url = '/erp/django_ajax/';
      var data = {}
      //console.log("This Link:"+url);
      //console.log($(this));
      //$('#results').addClass("whirl no overlay");
      $('#results').addClass("load3");
      //$('#results').isLoading({ text: "Loading", position: "inside" });
      axios.post(url, data,AXIOS_CONFIG).then(function (response) {
    		  console.log(response.data);
          widget = response.data
          $('#results').removeClass("whirl no overlay");
          $('#results').html(widget);
    	  });
     });
});


function user_ajax(type,user){
  console.log("user:"+user);
  var URL = USER_URL + USER_CONFIG[type].url;
  axios.post(URL, {
    username: user
  },AXIOS_CONFIG)
  .then(function (response) {
    if(response.data.code==0){
      USER_FLAG = 1;
      notice('ok',JSON.stringify(response.data));
      console.log(response);
    }else{
      notice("操作失败.");
    }
    USER = '';
  });
};

// 添加用户
function customer_add_ajax(){
  var data = new FormData($(this));
  data.append("username", $("#id_username").val());
  data.append("password",$("#id_password").val());
  //data.append("confirm_password",$("#id_confirm_password").val());
  console.log("data:"+data)
  $.ajax({
      url:'/erp/customer_add/',
      type: 'POST',
      data: data,
      cache:false,
      processData: false,
      contentType: false,
      //part related to Django crsf token
      beforeSend: function(xhr, settings) {
          var csrftoken = getCookie('csrftoken');
          console.log("TOken:"+csrftoken)
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
      },
      success: function(data){
          var parseData = $.parseJSON(data);
          console.log(parseData.message);
      }
    });
}

// 删除用户
function user_remove(type){
  $("#userlist tr button").each(function (i) {
    $(this).click(function(){
      console.log("Origin User Value:"+USER);
      USER=$(this).parents("tr").attr('name')
      console.log("索引："+$(this).index()+"\nUser:"+USER);
      //alert("内容："+$(this).parents("tr").html());
     });
  });
};

// 修改密码
function setPassword(){
  var url = '/erp/set_password/'
  var username = $("#username").text();
  var old_password = $("#old_password").val();
  var new_password = $("#new_password").val();
  var confirm_password = $("#confirm_password").val();
  var data = {
    username:username,
    password:old_password,
    new_password:new_password,
    confirm_password:confirm_password
  }
	console.log("Data:");
  console.log(data);
	axios.post(url, data,AXIOS_CONFIG).then(function (response) {
    if(response.data.error == 0){
      console.log("Success Response....");
      toastr.success(response.data.msg)
      setTimeout("redirect_to_login()", 1500);

    }else{
      toastr.info(response.data.msg);
    }
		  console.log(response);
	  });
	};

  // 注册用户
  function register(){
    var url = '/erp/register/'
    //var username = $
  }

/********************** AJax Events **********************/
// Ajax x-www-form
function form_ajax(url){
  var data = new FormData($('#addUser form')[0]);
	console.log("Data:")
  console.log(data);
	axios.post(url, data,AXIOS_CONFIG).then(function (response) {
		  console.log(response);
	  });
	};
$(document).ready(function(){
  // 修改密码(AJAX)
  $("#setPassword button.confirm").click(function(){
      setPassword(CURRENT_USER);
  });

});



/************************************************************/

$('#form11').submit(function(e){
        e.preventDefault();

        //fill FormData with form fields

        var data = new FormData($(this));
        data.append("photo", $("#id_photo")[0].files[0]);
        data.append("description",$("#id_description").val());

        $.ajax({
            url:'/erp/customer_add/',
            type: 'POST',
            data: data,
            cache:false,
            processData: false,
            contentType: false,
            //part related to Django crsf token
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                 // Send the token to same-origin, relative URLs only.
                 // Send the token only if the method warrants CSRF protection
                 // Using the CSRFToken value acquired earlier
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                  }
            },
            success: function(data){
                var parseData = $.parseJSON(data);
                console.log(parseData.message);
            }
        });

    });


function form_ajax2() {
    var settings = {csrfmiddlewaretoken: '{{ csrf_token }}'}
    console.log("Your are here...csrf_token: "+data.csrfmiddlewaretoken)

    var name = $("#id_username").val();                 //获得form中用户输入的name 注意这里的id_name 与你html中的id一致
    var password = $("#id_password").val();    //同上

    $.ajax({
        type:"POST",
        data: {username:name, password:password},
        url: "/erp/ajax_test/", //后台处理函数的url 这里用的是static url 需要与urls.py中的name一致
        cache: false,
        dataType: "html",
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
             // Send the token to same-origin, relative URLs only.
             // Send the token only if the method warrants CSRF protection
             // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
              }
        },
        success: function(result, statues){
            toastr(result);                                         //成功时弹出view传回来的结果
        },
        error: function(){
            toastr("false...");
        }
    });
};



/******************* Test ********************/
function ajax_test(){
  axios.post('/erp/ajax_test/', {a: 1, b:2}, {
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
  }).then(response => response.data)
    .then(data => {
      console.log(data);
      notice('ok',JSON.stringify(data));
    });
}

/**************** Test *************************/
function create_post() {
    console.log("create post is working!") // sanity check
    console.log("Post_text:"+$('#id_post_text').val())
    $.ajax({
        url : "/erp/create_post/", // the endpoint
        type : "POST", // http method
        data : { the_post : $('#id_post_text').val() }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            $('#post-text').val(''); // remove the value from the input
            console.log(json); // log the returned json to the console
            notice('ok',JSON.stringify(json))
            $("#talk").prepend("<li><strong>"+json.text+"</strong> - <em> "+json.author+"</em> - <span> "+json.created+"</span></li>");
            console.log("success"); // another sanity check
        },
        beforeSend: function(xhr, settings) {
            var csrftoken = getCookie('csrftoken');
            console.log("Cookie:"+csrftoken)
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};
$(document).ready(function(){
  $('#post-form').on('submit', function(event){
      console.log("Here...")
      event.preventDefault();
      console.log("form submitted!")  // sanity check
      create_post();
  });
});
