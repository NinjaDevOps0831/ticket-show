<template>
  <div class="container row">
    <div class="col-md-8">
      <table class="table table-striped">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Name</th>
            <th scope="col">Place</th>
            <th scope="col">Capacity</th>
          </tr>
        </thead>
        <tbody>
          <tr></tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from "../../services/axios-config";

export default {
  name: "TheatreListComponent",
  data() {
    return {
      theatreList: [],
    };
  },
  created() {
    const API_URL = "http://localhost:5000/api/theatres/";

    axios
      .get(API_URL)
      .then((response) => {
        this.theatreList = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  },
  methods: {},
};
</script>

<style></style>
