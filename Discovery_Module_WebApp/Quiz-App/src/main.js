//imports from packages
import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from  'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

//use b-vue
Vue.use(BootstrapVue)

Vue.config.productionTip = false

//wheere to start rendering the vue instance
new Vue({
  render: h => h(App),
}).$mount('#app')
