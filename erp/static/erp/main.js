
// toastr 消息提示设置(已改用jquery toast)
toastr.options = {
        closeButton: false,
        debug: false,
        //progressBar: true,
        //positionClass: "toast-bottom-center",
		positionClass: "toast-top-center",
        onclick: null,
        showDuration: "300",
        hideDuration: "1000",
        timeOut: "2000",
        extendedTimeOut: "1000",
        showEasing: "swing",
        hideEasing: "linear",
        showMethod: "fadeIn",
        hideMethod: "fadeOut"
    };

// JQuery Toast wraper function
// 用于消息提示
function notice(type,msg){
  var type = arguments[0] ? arguments[0] : 'info';
  var msg = arguments[1] ? arguments[1] : '提示消息';
  var bgcolor='#337dac';
  var icon='info'
  switch(type)
  {
      case 'ok':
          bgcolor='#187d49';
          icon='success';
          break;
      case 'warn':
          bgcolor='#7d2a18';
          icon='warning';
          break;
  }
  $.toast({
    //heading: '操作结果',
    text: msg,
    position: 'top-center',
    icon: icon,
    bgColor: bgcolor,
    stack: false
  });
}

// ************Get csrf token for ajax************
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
//var csrftoken = getCookie('csrftoken');
// **** axios config
var AXIOS_CONFIG = {
  xsrfCookieName: 'csrftoken',
  xsrfHeaderName: 'X-CSRFToken'
}

// ******************** 用户管理 *****************
var USER = '';
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

// Ajax x-www-form
function form_ajax(url){
  var data = new FormData($('#addUser form')[0]);
	console.log("Data:")
  console.log(data);
	axios.post(url, data,AXIOS_CONFIG).then(function (response) {
		  console.log(response);
	  });
	};


  axios.post(authServerUrl + token_access_path,
      querystring.stringify({
              username: 'abcd', //gave the values directly for testing
              password: '1235!',
              client_id: 'user-client'
      }), {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded"
        }
      }).then(function(response) {
          console.log(response);
      });


$('#form').submit(function(e){
        e.preventDefault();

        //fill FormData with form fields

        var data = new FormData($(this));
        data.append("photo", $("#id_photo")[0].files[0]);
        data.append("description",$("#id_description").val());

        $.ajax({
            url:'/',
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
