document.getElementById('captureButton').addEventListener('click', () => {
    chrome.tabs.captureVisibleTab({ format: 'png' }, (dataUrl) => {
        const blob = dataURItoBlob(dataUrl);
        const blobUrl = URL.createObjectURL(blob);

        chrome.downloads.download({
            url: blobUrl,
            filename: 'fullmap_original.png', // Nome do arquivo a ser salvo
            conflictAction: 'overwrite', // Se o arquivo já existe, renomeia automaticamente
            saveAs: false, // Exibir janela de diálogo "Salvar como"
        });
    });
});

// Função auxiliar para converter data URL em Blob
function dataURItoBlob(dataURI) {
    const byteString = atob(dataURI.split(',')[1]);
    const mimeString = dataURI.split(',')[0].split(':')[1].split(';')[0];
    const ab = new ArrayBuffer(byteString.length);
    const ia = new Uint8Array(ab);
    for (let i = 0; i < byteString.length; i++) {
        ia[i] = byteString.charCodeAt(i);
    }
    return new Blob([ab], { type: mimeString });
}
