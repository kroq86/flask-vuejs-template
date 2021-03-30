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



