import { useLoaderData } from "@remix-run/react";
import { Badge } from "~/components/ui-library/badge";
import { Input } from "~/components/ui-library/input";
import { Label } from "~/components/ui-library/label";
import { ScrollArea } from "~/components/ui-library/scroll-area";
import { Separator } from "~/components/ui-library/separator";

export async function loader() {
    return {
        meta: {
            storageNode: "local-zephyr-pc",
            totalEnvs: 3
        },
        envs: [
            {
                name: "env-32.762",
                protocol: "v1"
            }, { name: "env-pagerank.v1", protocol: "v1" }, { name: "env-bq-batchProc.23", protocol: "v1" }
        ]
    }
}

export default function SelectEnvPage() {
    const savedEnvironments = useLoaderData<typeof loader>()

    return <>
        <div className="flex flex-col h-screen w-screen">
            <div className="basis-1/3">Select Environment</div>
            <div className="basis-2/3 flex flex-row">
                <div className="">
                    <div className="">Load Environment </div>
                </div>
                <div className="">
                    Create a new environment
                    <Label className="text-lg">Name</Label>
                    <Input />
                </div>
            </div>
        </div>
    </>
}