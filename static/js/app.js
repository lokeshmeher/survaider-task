'use strict';

var app = angular.module('topicsApp', []);

app.controller('MainController', function($scope, $http) {
	$scope.names = $http.get("/get_names").then(function(response) {
		return response.data.names;
	});

	// for (let name of $scope.names) {
	// 	console.log($scope.names);
	// }

	// $scope.watch('name', function() {
	// 	listNames();
	// });

	/* Initially `name` model is undefined. We set it to a random name and
	initialize the view which in turn invokes the `fetch()` callback. */
	// $scope.name = "Relina";

	// console.log($scope.names);

	// $scope.getTopics = function() {
	// 	;
	// }

	// $scope.getTopics();
});
