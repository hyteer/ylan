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
        timeOut: "4000",
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

// 序列化Form对象为JSON对象
$(function(){
    (function($){
        $.fn.serializeJson=function(){
            var serializeObj={};
            var array=this.serializeArray();
            var str=this.serialize();
            $(array).each(function(){
                if(serializeObj[this.name]){
                    if($.isArray(serializeObj[this.name])){
                        serializeObj[this.name].push(this.value);
                    }else{
                        serializeObj[this.name]=[serializeObj[this.name],this.value];
                    }
                }else{
                    serializeObj[this.name]=this.value;
                }
            });
            return serializeObj;
        };
    })(jQuery);
});

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

// 跳转到登录页
function redirect_to_login(){
  top.location.href="/erp/login";
}
