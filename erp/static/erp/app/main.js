define(function (require) {
    // Load any app-specific modules
    // with a relative require call,
    // like:
    var messages = require('./messages');

    // Load library/vendor modules using
    // full IDs, like:
    var print = require('print');

    print(messages.getHello());
    print(messages.ytInfo());

    var qs = require('qs');
    var obj = qs.parse('a=c');
    console.log(obj);

    var str = qs.stringify(obj);
    console.log(str);
    /*...
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
      */

});
