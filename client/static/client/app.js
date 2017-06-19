var app = angular.module('app', []);

app.controller('mainCtrl', ['$scope', '$http', '$interval', '$timeout', function($scope, $http, $interval, $timeout) {
    $scope.text = 'funkar';

    $interval(function() {
        if ($scope.admin && $scope.listing) {
            $scope.listLicenses();
        }
    }, 1000);

    function notifyExpiration() {
        $timeout(function() {
            if ($scope.rentedLicense) {
                alert('Your license "' + $scope.rentedLicense.identifier + '" has expired');
                $scope.rentedLicense = null;
            }
            $scope.errorMessage = '';
        }, 15000);
    }

    $scope.rentLicense = function() {
        $http.get('../license/rent/').then(function (result) {
            $scope.rentedLicense = result.data;
            notifyExpiration();
        }, function (error) {
            if (error.status === 404) {
                $scope.rentedLicense = null;
                $scope.errorMessage = 'No free licenses on server';
                notifyExpiration();
            } else {
                $scope.errorMessage = error.data;
                console.error('Couldn\'t retrieve any free license', error);
            }
        })
    }

    $scope.listLicenses = function() {
        $scope.listing = true;
        $http.get('../license/').then(function (result) {
            $scope.licenses = result.data;
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