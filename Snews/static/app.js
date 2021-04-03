var app = new Vue({
    el:'#app',
    delimiters: ['[[',']]'],
    data:{
        pb:{}
    },

    mounted: function () {
        this.fetchData();
    },
  
    methods: {
        fetchData: function () {
            this.$http.get(`/posts`).then(response => {
                this.pb = response.body; 
            }, response => {
                console.log("error"); 
            });
        },
    }
})

new Vue({
    el: '#app2',
    data: {
      message: 'Hello, i need smooth animation when text added(click me please)'
    },
    methods: {
        addText() {
      console.log('1');
          TweenLite.to(document.getElementById('test'), 2, {text:"This is animation with GSAP (vue plugin to animate anything) and i don't know how to animate it smooth", ease:Linear.easeNone});
      }
    }
  })
