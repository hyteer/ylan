
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
var USER = ''
var USER_DEL = ''
var USER_ADD = ''

function user_event(type){

  $("#userlist tr button").each(function (i) {
    $(this).click(function(){
      console.log("Origin User Value:"+USER_DEL);
      USER=$(this).parents("tr").attr('name')
      console.log("索引："+$(this).index()+"\nUser:"+USER);
      //alert("内容："+$(this).parents("tr").html());
      switch(type)
      {
          case 'add':
              USER_ADD = USER;
              break;
          case 'del':
              USER_DEL = USER;
              console.log("user.."+USER_DEL);
              break;
      }
     });
  });
};


function user_ajax(type,user){
  console.log("user:"+user);
  var baseurl = "/erp";
  switch(type)
  {
      case 'add':
          url=baseurl+"/customer_add/";
          msg='添加成功！';
          break;
      case 'del':
          url=baseurl+"/customer_del/";
          msg='删除成功！';
          break;
  }
  axios.post(url, {
    username: user
  },AXIOS_CONFIG)
  .then(function (response) {
    notice(msg,JSON.stringify(response.data));
    console.log(response);
  });
};
