//全局组件
Vue.component('coolBtn',{
						props: ['name','typee'],

						template:"<input @click='defaultClick' :class='typee' :value='name' type='button' style=\"color: #fff;border: none;padding: 2px 10px;border-radius: 6px;margin: 2px 6px;\">",
						methods: {
							defaultClick:function() {
								this.$emit('btn-click')
							},
	
						},
						created:function(){
							// alert("按钮初始化")
							if (!this.typee){
								this.typee='primary'
							}
						}
				});