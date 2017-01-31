module.exports = {
    entry: ['./app/main.js','./app/demo.js'],
    output: {
        path: './assets', // 输出文件的保存路径
        filename: 'bundle.js' // 输出文件的名称
    },
    module: {
      loaders: [
         {
           test: [/\.js$/, /\.es6$/],
           exclude: /node_modules/,
           loader: 'babel-loader',
           query: {
             presets: ['react', 'es2015']
           }
         },
         {
          test: /\.css$/,
          loader: 'style!css-loader?modules&importLoaders=1&localIdentName=[name]__[local]___[hash:base64:5]'
        }
       ]
    },
    resolve: {
      extensions: ['', '.js', '.es6']
    },
    //watch: true,

}
