<template>
  <div id="home-page">
      <h1> Trending </h1>
      <br>
      <!-- a select button for algorithm picker -->
      <b-form-select style="width:20%" v-model="algorithm" :options="['sedwik', 'twembeddings', 'algorithm 3','algorithm 4']" v-on:change="getEventSummary();" ></b-form-select>
    <br>
    <br>
        
    <div class="grid grid-cols-1 gap-4 px-4 mt-8 sm:grid-cols-4 sm:px-8">
        <div id=icon class="flex items-center bg-white border rounded-sm overflow-hidden shadow ">
            <div class="p-4 bg-blue-400">
                <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" class="bi bi-chat-left-text-fill" viewBox="0 0 16 16">
                    <path d="M0 2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H4.414a1 1 0 0 0-.707.293L.854 15.146A.5.5 0 0 1 0 14.793V2zm3.5 1a.5.5 0 0 0 0 1h9a.5.5 0 0 0 0-1h-9zm0 2.5a.5.5 0 0 0 0 1h9a.5.5 0 0 0 0-1h-9zm0 2.5a.5.5 0 0 0 0 1h5a.5.5 0 0 0 0-1h-5z"/>
                </svg>
            </div>

            <!-- Total tweets -->
            <div class="px-4 text-gray-700">
                <h3 class="text-sm tracking-wider">Total Tweets</h3>
                <p class="text-3xl">{{total_tweets}}</p>
            </div>
        </div>
        
        <div id=icon class="flex items-center bg-white border rounded-sm overflow-hidden shadow ">
            <div class="p-4 bg-blue-400">
                <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" class="bi bi-people-fill" viewBox="0 0 16 16">
                    <path d="M7 14s-1 0-1-1 1-4 5-4 5 3 5 4-1 1-1 1H7zm4-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"/>
                    <path fill-rule="evenodd" d="M5.216 14A2.238 2.238 0 0 1 5 13c0-1.355.68-2.75 1.936-3.72A6.325 6.325 0 0 0 5 9c-4 0-5 3-5 4s1 1 1 1h4.216z"/>
                    <path d="M4.5 8a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5z"/>
                </svg>
            </div>

            <!-- Total authors -->
            <div class="px-4 text-gray-700">
                <h3 class="text-sm tracking-wider">Total Autors</h3>
                <p class="text-3xl">{{total_autors}}</p>
            </div>
        </div>

        <div id=icon class="flex items-center bg-white border rounded-sm overflow-hidden shadow ">
            <div class="p-4 bg-blue-400">
                <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" class="bi bi-calendar2-week-fill" viewBox="0 0 16 16">
                    <path d="M3.5 0a.5.5 0 0 1 .5.5V1h8V.5a.5.5 0 0 1 1 0V1h1a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V3a2 2 0 0 1 2-2h1V.5a.5.5 0 0 1 .5-.5zm9.954 3H2.545c-.3 0-.545.224-.545.5v1c0 .276.244.5.545.5h10.91c.3 0 .545-.224.545-.5v-1c0-.276-.244-.5-.546-.5zM8.5 7a.5.5 0 0 0-.5.5v1a.5.5 0 0 0 .5.5h1a.5.5 0 0 0 .5-.5v-1a.5.5 0 0 0-.5-.5h-1zm3 0a.5.5 0 0 0-.5.5v1a.5.5 0 0 0 .5.5h1a.5.5 0 0 0 .5-.5v-1a.5.5 0 0 0-.5-.5h-1zM3 10.5v1a.5.5 0 0 0 .5.5h1a.5.5 0 0 0 .5-.5v-1a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5zm3.5-.5a.5.5 0 0 0-.5.5v1a.5.5 0 0 0 .5.5h1a.5.5 0 0 0 .5-.5v-1a.5.5 0 0 0-.5-.5h-1z"/>
                </svg>
            </div>

            <!-- Total events -->
            <div class="px-4 text-gray-700">
                <h3 class="text-sm tracking-wider">Total Events</h3>
                <p class="text-3xl">{{json_return.length}}</p>
            </div>
        </div>
    </div>

        
        
    <Graph :v-if="created" :json_data="json_return"></Graph>
    <br>
<br>
        <h3>All Events</h3>
        <!-- <div class="table">
                <b-table   :items="tweeetsInfo" :fields="fieldsTweetsInfo" striped responsive="sm" selectable @row-clicked="myRowClickHandler">
        </b-table>
        </div> -->
        <b-table fixed striped hover :items="json_return" :fields="fieldsTweetsInfo">
            <template #cell(num_of_tweets)="data">
                {{data.item.tweets.length}}
            </template>
            <template #cell(event)="data">
                <router-link :to="{ name: 'event', params: {id:data.item.event, tweets:data.item.tweets}}">
                    {{data.item.event}}
                </router-link>
            </template>
        </b-table>
    


  </div>
</template>

<script>
import Graph from "../components/graph.vue"
export default {
    name: "HomePage",
    components:{
        Graph
        
    },
    props: {
        algorithms:{
            type: Array,
            required: true
        }
    },
    data(){
        return{
            algorithm: "sedwik",
            total_autors:10000,
            total_tweets:39325000,
            total_events:28,
            created:false,
            sedweek:true,
            // json format for events/summary
            fieldsTweetsInfo:['event', 'num_of_tweets'],
            json_return:[],
            // json_return:[
            //     {
            //         event: "bla",
            //         tweets:[
            //             {
            //             id:"256292946331181056"
            //             },
            //             {
            //             id:"256334302034399232"
            //             },
            //             {
            //             id:"256335853738160128"
            //             },
            //             {
            //             id:"256346272506712064"
            //             },
            //             {
            //             id:"256346650132508673"
            //             },
            //         ],
            //         segmentation:"[take], [photo], [take a photo]"
            //     },
            //     {event: "bla1",
            //     tweets:[
            //         {
            //         id:"256292946331181056"
            //         },
            //         {
            //         id:"256334302034399232"
            //         },
            //         {
            //         id:"256335853738160128"
            //         },
            //         {
            //         id:"256346272506712064"
            //         },
            //         {
            //         id:"256346650132508673"
            //         },
            //     ],
            //     segmentation: "[mo yan], [chinese writer], [nobel prize literature]"}
            // ],
            //

            tweeetsInfo:[ {'event summary':'Take a photo','num of tweets':'4','Segmentation':"[take], [photo], [take a photo]"},
            {'event summary':'Chinese author Mo Yan wins the Nobel Prize in Literature','num of tweets':'2987','Segmentation':"[mo yan], [chinese writer], [nobel prize literature]"},
            {'event summary':'X Factor UK finalists James Arthur and Rylan Clark give a live show in London.','num of tweets':'1000','Segmentation':"[xfactor], [x factor], [james arthur], [rylan clark]"},
            {'event summary':'National Coming Out Day celebrated on this day.','num of tweets':'359','Segmentation':"[national coming out day], [national coming day], [lgbt], [coming day], [ncod]"},
            {'event summary':'Former US Senator Arlen Specter, died at the age of 82.','num of tweets':'4001','Segmentation':"[arlen specter], [passed away], [sen arlen specter]"},
            {'event summary':'Pop singer Taylor Swift performs live at the X Factor UK.','num of tweets':'892','Segmentation':"[taylor swift], [xfactor], [the x factor] "},
            {'event summary':'Every year, October is celebrated as Breast Cancer Awareness Month.','num of tweets':'1354','Segmentation':"[breast cancer awareness month], [breast cancer awareness], [cure cancer]"},
            {'event summary':'2nd US presidential debate between Barack Obama and Mitt Romney','num of tweets':'89','Segmentation':"[debate], [barack obama], [presidential debate]  "}]

        }
    },
    methods: {
        myRowClickHandler(record, index) {
            console.log(record); // This will be the item data for the row
            this.$router.push({ name: 'event', params: 1 });
        },
        async getEventSummary(){
            localStorage.setItem('algorithm',this.algorithm);
            try{
                const events = await this.axios.get(`http://127.0.0.1:5000/events/summary/${this.algorithm}`);
                this.json_return = events.data;
            } catch(error){
                this.json_return=require("../proccess_data.json")
                console.log(`error ${error}\noccured at getEventsSummary on HomePage.vue`);
            }
        }
    },
    created(){
        console.log("HomePage created");
        this.getEventSummary();
        localStorage.setItem('algorithm', this.algorithm);
        this.created=true;
    },


    
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Balsamiq+Sans&family=Merienda:wght@700&display=swap');
#home-page{
    font-family: 'Balsamiq Sans', cursive;
    /* font-family: 'Merienda', cursive; */
    text-align: center;
    background-color: whitesmoke;
        align-items: center;
        

}
#charts{
    margin-top: 3%;
    margin-left: 2%;
    display:flex;
}
.grid{
    display: flex;
}
#icon{
    display: flex;
    margin-left: 10px;
}
.table{
    overflow-x: scroll;
    overflow-y:scroll;
    margin: auto;
    height: 300px;


}
.b-table{
    background-color: white;
    opacity: 80%;

}
</style>