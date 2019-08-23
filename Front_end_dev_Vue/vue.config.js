module.exports = {
  publicPath: './',
  outputDir: '../Deploy/Front_end',
  productionSourceMap: false,
  devServer: {
    proxy: 'http://192.168.217.132'
  }
}
