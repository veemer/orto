var app = angular.module('orto', ['angularFileUpload', 'ngResource']);

// base config

app.config(['$httpProvider', '$interpolateProvider', function($httpProvider, $interpolateProvider) {

    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');

}]);


// constants

app.constant('AttachmentType', {
    planogramm: 'planogramm',
    topogramm: 'topogramm',
    R: 'R'
});

// services

app.service('Record', ['$resource', function($resource) {
    return $resource('/api/records/:id');
}]);

app.service('Attachments', ['$resource', function($resource) {
    return $resource('/api/records/:id/attachments');
}]);


// directives
app.directive('fileManager', function() {

    function controller($scope, $upload, $timeout) {

        $scope.description = '';
        $scope.fileReaderSupported = window.FileReader != null && (window.FileAPI == null || FileAPI.html5 != false);

        $scope.loading = false;

        $scope.save = function() {

            $scope.loading = true;

            for(var i=0; i<$scope.files.length; i++) {

                var file = $scope.files[i];

                $upload.upload({
                    url: $scope.getUrl(),
                    fields: {
                        'description': $scope.description,
                        'patient_id': $scope.patient,
                        'attachment_type': $scope.attachmentType
                    },
                    file: file,
                    fileFormDataName: 'attachment'
                }).success(function(data, status, headers, config) {

                    $scope.description = '';
                    $scope.attachments.push(data.attachment);
                    $scope.record = data.record;
                    $scope.files[0].dataUrl = null;

                    $scope.loading = false;

                });
            }
        }

        $scope.generateThumb = function(file) {
            if (file != null) {
                if ($scope.fileReaderSupported && file.type.indexOf('image') > -1) {
                    $timeout(function() {
                        var fileReader = new FileReader();
                        fileReader.readAsDataURL(file);
                        fileReader.onload = function(e) {
                            $timeout(function() {
                                file.dataUrl = e.target.result;
                            });
                        }
                    });
                }
            }
        }

        $scope.getUrl = function() {

            var url;

            if($scope.record.id) {
                url = '/api/records/'+$scope.record.id+'/attachments';
            }
            else {
                url = '/api/records/attachments'
            }

            return url;
        }

        $scope.$watch('files', function(files) {
            if (files != null) {
                for (var i = 0; i < files.length; i++) {
                    (function(file) {
                        $scope.generateThumb(file);
                    })(files[i]);
                }
            }
        });

    }

    function link(scope, element, attrs) {
        scope.title = attrs.title;
    }

    return {
        templateUrl: '/static/partials/file-manager.html',
        controller: ['$scope', '$upload', '$timeout', controller],
        link: link,
        scope: {
            record: '=',
            attachments: '=',
            attachmentType: '=',
            patient: '=',
        }
    }

});


app.directive('loadSpinner', [
    function () {
        return {
            restrict: "AE",
            transclude: true,
            template: '<div class="loading-spinner-parent">' +
                            '<div data-ng-show="loading" class="loading-spinner"></div>' +
                            '<div data-ng-transclude></div>' +
                        '</div>',
            scope: {
                loading: '=?'
            }
        };
    }
]);

// controllers

app.controller('StatusCtrl', ['$scope', '$upload', function($scope, $upload) {

    $scope.init = function(status) {
        $scope.status = status;
    }

    $scope.isActive = function(status) {
        return status == $scope.status;
    }

    $scope.setStatus = function(status) {
        $scope.status = status;
    }

}]);


app.controller('RecordCtrl', [
    '$scope', '$location', 'Record', 'Attachments', 'AttachmentType',
    function($scope, $location, Record, Attachments, AttachmentType) {

        $scope.AttachmentType = AttachmentType;

        $scope.record = {}

        $scope.planogramm_attachments = []
        $scope.topogramm_attachments = []
        $scope.R_attachments = []

        $scope.loading_record = false;
        $scope.save_record = false;
        $scope.load_attachments = false

        $scope.save = function() {

            $scope.save_record = true;

            var params = {}

            if($scope.record.id) {
                params.id = $scope.record.id;
            }

            Record.save(params, $scope.record, function(data) {
                $scope.record.id = data.record.id;
                $scope.save_record = false;
            });
        }

        $scope.loadRecord = function(recordId) {

            $scope.loading_record = true;

            if(recordId) {
                Record.get({'id': recordId}, function(data) {
                    $scope.record = data.record;
                    $scope.loading_record = false;
                })
            }

        }

        $scope.loadAttachments = function(recordId) {

            $scope.load_attachments = true

            if(recordId) {

                Attachments.get({'id': recordId}, function(data) {

                    data.attachments.forEach(function(attachment) {

                        if(attachment.attachment_type == AttachmentType.planogramm) {
                            $scope.planogramm_attachments.push(attachment);
                        }
                        else if(attachment.attachment_type == AttachmentType.topogramm) {
                            $scope.topogramm_attachments.push(attachment);
                        }
                        else if(attachment.attachment_type == AttachmentType.R) {
                            $scope.R_attachments.push(attachment);
                        }

                    });

                    $scope.load_attachments = false;

                });

            }

        }

        $scope.load = function(recordId) {
            $scope.loadRecord(recordId);
            $scope.loadAttachments(recordId);
        }

    }
]);