var app = angular.module('orto', []);

app.controller('StatusCtrl', ['$scope', function($scope) {

    $scope.init = function(status) {
        console.log(status);
        $scope.status = status;
    }

    $scope.isActive = function(status) {
        return status == $scope.status;
    }

    $scope.setStatus = function(status) {
        $scope.status = status;
    }

}]);
