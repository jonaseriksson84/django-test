var app = angular.module('app', []);

app.controller('mainCtrl', ['$scope', '$http', '$interval', function($scope, $http, $interval) {
    $scope.text = 'funkar';

    $interval(function() {
        if ($scope.admin && $scope.listing) {
            $scope.listLicenses();
        }
    }, 1000);

    $scope.listLicenses = function() {
        $scope.listing = true;
        $http.get('../license/').then(function (result) {
            $scope.licenses = result.data.results;
        }, function (error) {
            console.error('Couldn\'t retrieve licenses', error);
        });
    }

    $scope.addLicense = function() {
        var data = {
            identifier: $scope.identifier,
            rented: false,
            rent_date: null
        };
        $http.post('../license/', data).then(function (result) {
            $scope.identifier = '';
            $scope.addDialog = false;
            $scope.errorMessage = '';
        }, function (error) {
            $scope.errorMessage = error.data.identifier[0];
            console.error('Couldn\'t add license', error);
        });
    }

}]);