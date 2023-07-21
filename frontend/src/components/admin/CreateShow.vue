<template>
  <div class="container row">
    <div class="col-md-8 col-off-set-2">
      <form @submit.prevent="handleForm">
        <div class="mb-3">
          <label for="name" class="form-label">Name</label>
          <input
            v-model="theatre.name"
            type="text"
            class="form-control"
            id="name"
          />
        </div>
        <div class="mb-3">
          <label for="place" class="form-label">Place</label>
          <input
            v-model="theatre.place"
            type="text"
            class="form-control"
            id="place"
          />
        </div>
        <div class="mb-3">
          <label for="capacity" class="form-label">Capacity</label>
          <input
            v-model="theatre.capacity"
            type="number"
            class="form-control"
            id="capacity"
          />
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </div>
  </div>
</template>

<script>
import Theatre from "../../models/theatre";
import axios from "../../services/axios-config";

export default {
  name: "CreateTheatreComponent",
  data() {
    return {
      theatre: new Theatre("", "", 0),
    };
  },
  methods: {
    handleForm() {
      const API_URL = "http://localhost:5000/api/theatres/";

      axios
        .post(API_URL, {
          name: this.theatre.name,
          place: this.theatre.place,
          capacity: this.theatre.capacity,
        })
        .then((response) => {
          console.log(response.data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style></style>
