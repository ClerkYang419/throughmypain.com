<!--barchart single-file-component-->
<!--temporarily not in use-->

<template id="tem-barChart">
        <section class="uk-section uk-section-muted uk-margin uk-box-shadow-small">
                <div class="chart uk-width-1-2">

                </div>
                <div class="chart"></div>
                <div class="uk-width-1-2 uk-float-right">
                
                    <label>Object:</label>
                    <div class="radio-group uk-margin-remove-left uk-float-right uk-margin-large-right" >
                        <input id="All" v-model="object" value="All pain" class="uk-radio" type="radio" name="All">
                        <label for="All" style="padding: 3px 30px">All pain</label>
                        <input id="Individual" v-model="object" value="Individual pain" class="uk-radio" type="radio" name="Individual">
                        <label for="Individual" style="padding: 3px 10px">Individual pain</label>
                    </div>
                    
                    <div class="uk-margin">
                        <label>Pain ID:</label><input v-bind:value="painid" class="uk-input uk-form-small uk-form-width-small uk-float-right uk-margin-large-right">
                    </div>
    
                    <div class="uk-margin">
                        <label>Dependent variable:</label>
                        <select v-model="d_variable" class="uk-select uk-form-small uk-form-width-small uk-float-right uk-margin-large-right">
                            <option v-for="variable of dvariables" v-bind:key="variable" v-text="variable"></option>
                        </select>
                    </div>
                    
                    <div class="uk-margin">
                        <label>Independent variable:</label>
                        <select v-model="i_variable" class="uk-select uk-form-small uk-form-width-small uk-float-right uk-margin-large-right">
                            <option v-for="variable of ivariables" v-bind:key="variable" v-text="variable"></option>
                        </select>
                    </div>
                    
                    <div class="uk-margin">
                        <input v-model="date_in" class="datepicker uk-input uk-form-small uk-form-width-small"><span :uk-icon="'calendar'"></span>
                        &nbsp; to &nbsp;
                        <input v-model="date_out" class="datepicker uk-input uk-form-small uk-form-width-small"><span :uk-icon="'calendar'"></span>
                    </div>
                    
                </div>
            </section>
</template>

<script>
module.exports = {
    delimiters: ["[[", "]]"],
    data:function(){
        return {
            object:"",
            pain_id:"",
            d_variable:"",
            i_variable:"",
            date_in:"",
            date_out:"",
            chart_data:[30, 86, 168, 281, 303, 365]
        }
    },
    props:[
                'painid',
                'dvariables',
                'ivariables',
                'data'
            ]
}

d3.select(".chart")
        .selectAll("div")
        .data(this.$data.chart_data)
        .enter()
        .append("div")
        .style("width", function(d) { return d + "px"; })
        .text(function(d) { return d; }); 
</script>

<style scoped>
.chart div{
    font: 10px sans-serif;
    background-color: steelblue;
    text-align: right;
    padding: 3px;
    margin: 1px;
    color: white;
  }
</style>

