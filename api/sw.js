self.addEventListener('install', function (e) {
    console.log("[Service Worker] Install");
});
self.addEventListener('fetch', function (e) {
    console.log("[Service Worker] Fetched resource " + e.request.url);
});

self.addEventListener('push', event => {
    const data = event.data ? event.data.json() : {};
    const title = data.title || 'プッシュ通知';
    const options = {
        body: data.body || 'プッシュ通知の本文',
        icon: data.icon || '/static/icons/HauCIeD9yRG3SEM1740368341_1740368455.png',
    };
    event.waitUntil(self.registration.showNotification(title, options));
});

self.addEventListener('notificationclick', event => {
    event.notification.close();
    event.waitUntil(clients.matchAll({ type: "window" }).then(clientList => {
        if (clientList.length > 0) {
            return clientList[0].focus();
        }
        return clients.openWindow('/');
    }));
});