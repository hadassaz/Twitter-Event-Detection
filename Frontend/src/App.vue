<template>
  <div id="app">
    <!-- <b-navbar toggleable type="dark" variant="dark">
        <b-navbar-brand :to='{ name: "home" }'>Twitter Event Detection</b-navbar-brand>
        <b-button v-b-toggle.sidebar-1>Toggle Sidebar</b-button> -->
      <b-row>
        <b-col>
          <!-- static sidebar -->
          <b-sidebar id="sidebar-border" sidebar-class="border-right border-light" bg-variant="info" text-variant="light"
           title="Twitter Event Detection" no-close-on-route-change="true" no-close-on-esc="true" no-header-close="true"
            visible="true">
            <b-navbar-nav id="nav-items" class="ml-auto">
              <b-nav-item :to='{ name: "home" }'>
                <b-icon-graph-up></b-icon-graph-up> Trending
              </b-nav-item>
              <b-nav-item href="#">
                <b-icon-signpost-split></b-icon-signpost-split> Compare
              </b-nav-item>
              <b-nav-item :to="{ name: 'events'}">
                <b-icon-list-ul></b-icon-list-ul> Events
              </b-nav-item>
              <!-- <b-nav-item :to="{ name: 'event', params:{id:123}}"> Event </b-nav-item> -->
              
              <b-nav-item href="#">
                <b-icon-person-circle></b-icon-person-circle> Login
              </b-nav-item>
            </b-navbar-nav>
              <!-- <template #footer="{ hide }">
                <div class="d-flex bg-light text-dark align-items-center px-3 py-2">
                  <strong class="mr-auto">© Shorlak members</strong>
                  <b-button size="sm" @click="hide">Close</b-button>
                </div>
              </template> -->
          </b-sidebar>
        </b-col>
        <b-col cols="10">
          <router-view />
        </b-col>
     </b-row>

      <!-- <b-navbar-toggle v-b-toggle.sidebar-footer target="sidebar-footer">
        <template #default="{ expanded }">
            <b-icon v-if="expanded" icon="chevron-bar-up"></b-icon>
            <b-icon v-else icon="chevron-bar-down"></b-icon>
        </template>
      </b-navbar-toggle>
    </b-navbar> -->
    
  </div>
</template>

<script>
export default {
  name: "App",
};
</script>

<style lang="scss">
@import "./scss/form-style.scss";

#sidebar-border{
  text-align: center;
  width: 17%;
}

#nav-items a{
  color: white;
}

#nav-items a:hover{
  color: black;
}
</style>