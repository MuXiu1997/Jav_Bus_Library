module.exports = {
  presets: [
    '@vue/app'
  ],
  'plugins': [
    '@babel/plugin-syntax-dynamic-import',
    [
      'component',
      {
        'libraryName': 'element-ui',
        'styleLibraryName': 'theme-chalk'
      }
    ]
  ]
}
